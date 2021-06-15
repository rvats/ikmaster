using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Fairway.Controllers
{
    public interface IBorrowerRepository
    {
        Task GetBorrowerTransactionsAsync(List<int> borrowerIds, string dateTime1, string dateTime2);

    }
}