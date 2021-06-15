using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Web.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using HttpGetAttribute = System.Web.Http.HttpGetAttribute;
using RouteAttribute = System.Web.Http.RouteAttribute;

namespace Fairway.Controllers
{
    [ApiController]
    [System.Web.Http.Route("[controller]")]
    public class LoanTransactionController : ControllerBase
    {
        private readonly IBorrowerRepository _borrowerRepository;
        private readonly ILogger<LoanTransactionController> _logger;

        public LoanTransactionController(ILogger<LoanTransactionController> logger, IBorrowerRepository borrowerRepository)
        {
            _logger = logger;
            _borrowerRepository = borrowerRepository
        }

        [HttpGet, Route("/v1/loan/{loanId}/transactions/startDate/{startDate}/endDate/{endDate}")]
        public async Task<IHttpActionResult> Get(List<int> borrowerIds, DateTime dateStart, DateTime dateEnd)
        {
            try
            {
                IList<LoanTransaction> transactions = new List<LoanTransaction>();
                foreach (var borrowerId in borrowerIds)
                {
                    // Make a call to /v1/borrower/{borrowerId}/loans 
                    //                /v1/borrower/{borrowerId}/loans
                    var loanTransactions = await _borrowerRepository.GetBorrowerTransactionsAsync(borrowerIds, dateStart.ToUniversalTime(), dateEnd.ToUniversalTime());
                    transactions.Add(borrowerLoanTransactions);
                }
                

                return Ok(transactions);
            }
            catch (Exception ex)
            {
                return NotFound();
            }
        }
    }
}
